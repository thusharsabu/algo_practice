from confluent_kafka import SerializingProducer


class KafkaProducer:

    def kafkaConfigs(self):
        return {
            "bootstrap.servers": self.get_variable("keyName"),
            #
            #
            #
            #
            # Add All configs here
        }

    def delivery_report(err, msg):
        if err:
            # cust_logger_exec.error('%% Message failed delivery: %s\n' % err)
            print("%% Message failed delivery: %s\n" % err)
        else:
            # self.cust_logger_exec.error('%% Message delivered to %s [%d] @ %d\n' %
            #                   (msg.topic(), msg.partition(), msg.offset()))
            print(
                "%% Message delivered to %s [%d] @ %d\n"
                % (msg.topic(), msg.partition(), msg.offset())
            )

    # Format the message based on type of data
    def messageNormalizer(self, message):
        return [message]

    def kafkaProducer(self, message):
        producerConfig = self.kafkaConfigs()
        topic = self.get_variable("topic")

        producer = SerializingProducer(**producerConfig)

        splittedMessage = self.messageNormalizer(message)

        for eachMessage in splittedMessage:
            key = None

            producer.produce(
                topic=topic, key=key, value=eachMessage, on_delivery=self.delivery_report
            )

            producer.poll(0.0)
        producer.flush()
