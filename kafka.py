from confluent_kafka import SerializingProducer


class KafkaProducer:
    def kafkaConfigs(self):
        return {
            # "bootstrap.servers": self.get_variable("keyName"),
            #
            # Add All configs here

            'bootstrap.servers': 'kfkws...' # Populate as it is
        }

    def delivery_report(err, msg):
        if err:
            # cust_logger_exec.error('%% Message failed delivery: %s\n' % err)
            print("%% Message failed delivery: %s\n" % err)
        else:
            # self.cust_logger_exec.error('%% Message delivered to %s [%d] @ %d\n' %
            #                   (msg.topic(), msg.partition(), msg.offset()))
            print(
                # self.cust_logger_exec.info('')
                "%% Message delivered to %s [%d] @ %d\n"
                % (msg.topic(), msg.partition(), msg.offset())
            )

    # Format the message based on type of data
    def messageSanitizer(self, message):
        return message

    # Format message based on requirements
    def messageFormatter(self, msg):
        # 1. Validate Message
        # 2. Format Message if given formatter
        return msg

    def kafkaProducer(self, messages):
        if messages is None or len(messages) == 0:
            return  # Raise expeception in production ArguementError

        producerConfig = self.kafkaConfigs()
        topic = self.get_variable("topic")

        producer = SerializingProducer(**producerConfig)

        sMessages = self.messageSanitizer(messages)

        for message in sMessages:
            try:
                key = None

                formatedMsg = self.messageFormatter(message)

                producer.produce(
                    topic=topic,
                    key=key,
                    value=formatedMsg,
                    on_delivery=self.delivery_report,
                )

                producer.poll(0.0)
            except Exception as e:
                # log error to logger
                print(f"Failed to produce: {e}")

        producer.flush()



kp = KafkaProducer()
sampleMessage = [{'key1': 'Some data', 'key2': 'Some data 2'}]

kp.kafkaProducer(sampleMessage)
