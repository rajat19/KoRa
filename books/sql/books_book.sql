-- Adminer 4.3.1 PostgreSQL dump

DROP TABLE IF EXISTS "books_book";
CREATE SEQUENCE books_book_id_seq INCREMENT  MINVALUE  MAXVALUE  START 1 CACHE ;

CREATE TABLE "public"."books_book" (
    "id" integer DEFAULT nextval('books_book_id_seq') NOT NULL,
    "title" character varying(250) NOT NULL,
    "language" character varying(100),
    "genre" character varying(200) NOT NULL,
    "synopsis" text NOT NULL,
    "year" character varying(4),
    "logo" character varying(300) NOT NULL,
    "logo_file" character varying(100) NOT NULL,
    "author_id" integer NOT NULL,
    "series_id" integer,
    CONSTRAINT "books_book_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "books_book_title_author_id_9cf77801_uniq" UNIQUE ("title", "author_id"),
    CONSTRAINT "books_book_author_id_8b91747b_fk_books_bookauthor_id" FOREIGN KEY (author_id) REFERENCES books_bookauthor(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE,
    CONSTRAINT "books_book_series_id_6f42ccc1_fk_books_bookseries_id" FOREIGN KEY (series_id) REFERENCES books_bookseries(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE
) WITH (oids = false);

CREATE INDEX "books_book_author_id_8b91747b" ON "public"."books_book" USING btree ("author_id");

CREATE INDEX "books_book_series_id_6f42ccc1" ON "public"."books_book" USING btree ("series_id");

INSERT INTO "books_book" ("id", "title", "language", "genre", "synopsis", "year", "logo", "logo_file", "author_id", "series_id") VALUES
(1,	'Immortals Of Meluha',	NULL,	'History',	'The Immortals of Meluha is the first novel of the Shiva trilogy series by Amish Tripathi. The story is set in the land of Meluha and starts with the arrival of the Shiva. The Meluhans believe that Shiva is their fabled saviour Neelkanth. Shiva decides to help the Meluhans in their war against the Chandravanshis, who had joined forces with a cursed Nagas; however, during his journey and the fight that ensues, Shiva learns how his choices actually reflect who he aspires to be and how they lead to dire consequences.',	NULL,	'',	'/book/logo/cover.jpg',	1,	NULL);

-- 2018-01-02 12:19:07.435438+05:30
