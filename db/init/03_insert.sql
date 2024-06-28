INSERT INTO member (name) VALUES ('tanaka');
INSERT INTO member (name) VALUES ('suzuki');
INSERT INTO member (name) VALUES ('satou');
INSERT INTO member (name) VALUES ('kimura');

INSERT INTO agenda (topic, start_date) VALUES ('議題A', '2024-03-21');


INSERT INTO opinion (member_id, is_approve, topic_id) VALUES (3, TRUE, 1);
INSERT INTO opinion (member_id, is_approve, topic_id) VALUES (1, FALSE, 1);
INSERT INTO opinion (member_id, is_approve, topic_id) VALUES (2, TRUE, 1);


