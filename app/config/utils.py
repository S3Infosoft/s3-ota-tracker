from django.utils.timezone import now
from json_log_formatter import JSONFormatter


class CustomJSONFormat(JSONFormatter):

    def json_record(self, message, extra, record):
        if 'time' not in extra:
            extra['time'] = now()

        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)

        return extra
