import time
from elastalert.alerts import Alerter, BasicMatchString


class AlertaFichero(Alerter):

    required_options = set(['message_alert','output_file_path'])


    def alert(self, matches):

        # Matches is a list of match dictionaries.
        # It contains more than one match when the alert has
        # the aggregation option set
        for match in matches:

            # Config options can be accessed with self.rule
            with open(self.rule['output_file_path'], "a") as output_file:
                ts = time.time()
                readable_time = time.ctime(ts)
                match_string = str(BasicMatchString(self.rule, match))

                fichero = str(self.rule['message_alert'])
                output_file.write(readable_time + fichero + match_string + '\n')
    # get_info is called after an alert is sent to get data that is written back
    # to Elasticsearch in the field "alert_info"
    # It should return a dict of information relevant to what the alert does
    def get_info(self):	
        return {'type': 'AlertaFichero',
                'output_file': self.rule['output_file_path']}