from django.db import models
from django.utils.translation import gettext_lazy as _


class ValueType(models.Model):
    """Model that represents type of indicator value."""

    name = models.CharField(
        verbose_name=_('value type name'),
        max_length=100,
        unique=True
    )

    class Meta:
        verbose_name = _('value type')
        verbose_name_plural = _('value types')

    def __str__(self) -> str:
        return self.name


class Indicator(models.Model):
    """Model that represents key performance indicator of entity."""

    name = models.CharField(
        verbose_name=_('indicator name'),
        max_length=500,
        unique=True
    )
    annotation = models.CharField(
        verbose_name=_('annotation'),
        max_length=500,
        blank=True
    )
    value_type = models.ForeignKey(
        verbose_name=_('value type'),
        to=ValueType,
        on_delete=models.RESTRICT
    )
    staff_only_editable = models.BooleanField(
        verbose_name=_('staff only editable'),
        default=False
    )

    class Meta:
        verbose_name = _('indicator')
        verbose_name_plural = _('indicators')

    def __str__(self) -> str:
        return self.name


class RatingPartition(models.Model):
    """Model that represents group of criterions of similar indicators."""

    name = models.CharField(
        verbose_name=_('rating partition name'),
        max_length=100,
        unique=True
    )
    abbreviation = models.CharField(
        verbose_name=_('rating partition abbreviation'),
        max_length=5,
        unique=True
    )
    indicators = models.ManyToManyField(
        verbose_name='rating partition criterions',
        to=Indicator,
        through='Criterion',
        related_name='partitions'
    )

    class Meta:
        verbose_name = _('rating partition')
        verbose_name_plural = _('rating partitions')

    def __str__(self):
        return self.name


class Criterion(models.Model):
    """Model that represents indicator in a specific rating partition."""

    indicator = models.ForeignKey(
        verbose_name=_('criterion indicator'),
        to=Indicator,
        on_delete=models.CASCADE
    )
    partition = models.ForeignKey(
        verbose_name=_('criterion partition'),
        to=RatingPartition,
        on_delete=models.CASCADE
    )
    number = models.IntegerField(verbose_name=_('criterion number'))
    subnumber = models.IntegerField(
        verbose_name=_('criterion subnumber'),
        blank=True,
        null=True
    )
    weight = models.FloatField(verbose_name=_('criterion weight'))

    class Meta:
        verbose_name = _('criterion')
        verbose_name_plural = _('criterions')

    def __str__(self) -> str:
        if self.subnumber:
            return (f'{self.partition.abbreviation}.{self.number}'
                    f'.{self.subnumber} {self.indicator}')
        else:
            return (f'{self.partition.abbreviation}.{self.number}'
                    f' {self.indicator}')
