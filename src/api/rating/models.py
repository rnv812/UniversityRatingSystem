from django.db import models
from django.utils.translation import gettext_lazy as _


class ValueType(models.Model):
    """Model represents type of indicator value."""

    class DataTypes(models.TextChoices):
        BOOL = 'bool', _('boolean')
        INT = 'int', _('integer')
        FLOAT = 'float', _('float')
        STR = 'str', _('text')

    name = models.CharField(
        verbose_name=_('value type name'),
        max_length=100,
        unique=True
    )

    datatype = models.CharField(
        verbose_name=_('data type'),
        choices=DataTypes.choices,
        max_length=5
    )

    class Meta:
        verbose_name = _('value type')
        verbose_name_plural = _('value types')

    def __str__(self) -> str:
        return self.name


class Indicator(models.Model):
    """Model represents key performance indicator of educator,
    department or faculty.
    """

    name = models.CharField(
        verbose_name=_('indicator name'),
        max_length=500,
        unique=True
    )
    annotation = models.CharField(
        verbose_name=_('indicator annotation'),
        max_length=500,
        blank=True
    )
    value_type = models.ForeignKey(
        verbose_name=_('indicator value type'),
        to=ValueType,
        on_delete=models.RESTRICT
    )
    privileged = models.BooleanField(
        verbose_name=_('indicator privileged status'),
        default=False
    )

    class Meta:
        verbose_name = _('indicator')
        verbose_name_plural = _('indicators')

    def __str__(self) -> str:
        return self.name


class RatingPartition(models.Model):
    """Model represents group of criterions of similar indicators."""

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
    """Model represents indicator in a specific rating partition. Criterion
    in addition to Inicator has weight of the influency for the speficified
    partition and its own number and subnumber inside partition.
    """

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
