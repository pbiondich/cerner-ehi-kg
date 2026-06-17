# AP_CASE_QUERY_DETAILS

> This reference table contains detail informations associated with a Pathology Report Query. Other parameters about the query are stored on the AP_Case_Query.

**Description:** AP Case Query Details  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_VALUE_DISP` | VARCHAR(40) |  |  | This field contains the display value of the beginning query value within a specified query parameter (denoted in the PARAM_NAME field), if defined. |
| 2 | `BEG_VALUE_DT_TM` | DATETIME |  |  | This field contains the date and time of the beginning query value within a specified query parameter (denoted in the PARAM_NAME field), if defined. |
| 3 | `BEG_VALUE_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the beginning query value within a specified query parameter (denoted in the PARAM_NAME field), if defined. |
| 4 | `CASE_QUERY_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code which uniquely identifies the case retrieval query (and its associated parameters). This value is used to join to other tables, such as the AP_CASE_QUERY table. |
| 5 | `CRITERIA_TYPE_FLAG` | DOUBLE |  |  | This field contains a representation of the type of parameters included in the query -- case, patient, or criteria -- included on this row within the diagnostic query table. One query may be represented by multiple rows. |
| 6 | `DATE_TYPE_FLAG` | DOUBLE |  |  | This field contains a representation of the type of date included in this query parameter -- range, previous dates, months, or years. |
| 7 | `END_VALUE_DISP` | VARCHAR(40) |  |  | This field contains the display value of the ending query value within a specified query parameter (denoted in the PARAM_NAME field), if defined. |
| 8 | `END_VALUE_DT_TM` | DATETIME |  |  | This field contains the date and time of the ending query value within a specified query parameter (denoted in the PARAM_NAME field), if defined. |
| 9 | `END_VALUE_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the ending query value within a specified query parameter (denoted in the PARAM_NAME field), if defined. |
| 10 | `FREETEXT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the LONG_TEXT table that contains the free textsearch value. |
| 11 | `FREETEXT_QUERY_FLAG` | DOUBLE |  |  | This field determines whether free textsearching crosses multiple paragraphs or within a paragraph. |
| 12 | `NEGATION_IND` | DOUBLE |  |  | This field is not used at this time. |
| 13 | `PARAM_NAME` | VARCHAR(20) |  |  | This field represents the type of query criteria (collection date, diagnostic code, patient age, for example) associated with this row on the diagnostic query parameters table. |
| 14 | `QUERY_DETAIL_ID` | DOUBLE | NOT NULL |  | This field is the unique identifier to the AP_CASE_QUERY_DETAILS table |
| 15 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field, in conjunction with the value included in the CASE_QUERY_ID field, uniquely identifies a row on this table. |
| 16 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the diagnostic coding "vocabulary", if defined. Multiple vocabularies, such as SNOMED II and SNOMED III, might reside on a single system. |
| 17 | `SYNOPTIC_CCL_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the long_text table that contains the synoptic search query in ccl format. |
| 18 | `SYNOPTIC_QUERY_FLAG` | DOUBLE | NOT NULL |  | This field determines the type of synoptic query that is to be performed. |
| 19 | `SYNOPTIC_XML_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the long_text table that contains the synoptic search query in xml format. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_QUERY_ID` | [AP_CASE_QUERY](AP_CASE_QUERY.md) | `CASE_QUERY_ID` |
| `FREETEXT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SYNOPTIC_CCL_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SYNOPTIC_XML_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

