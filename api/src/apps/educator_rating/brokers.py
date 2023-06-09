from abc import ABC

from .models import EducatorReport
from .convertions import bundle_report


class BrokerService(ABC):
    ...


class RabbitMQBrokerService(BrokerService):
    ...


def send_educator_report_to_broker(
    report: EducatorReport,
    broker: BrokerService
):
    data = bundle_report(report)
    # broker.send(data)
