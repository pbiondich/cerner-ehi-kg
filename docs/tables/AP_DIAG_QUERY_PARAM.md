# AP_DIAG_QUERY_PARAM

> This reference table includes Diagnostic Reporting query parameters that have been established and saved. Using these parameters, the same report can be run multiple times, by different users.

**Description:** AP Diagnostic Reporting Query Parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_VALUE_DT_TM` | DATETIME |  |  | This field contains the date and time of the beginning query value within a specified query parameter (denoted in the PARAM_NAME field), if defined. |
| 2 | `BEG_VALUE_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the beginning query value within a specified query parameter (denoted in the PARAM_NAME field), if defined. |
| 3 | `CRITERIA_TYPE_FLAG` | DOUBLE |  |  | This field contains a representation of the type of parameters included in the query -- case, patient, or criteria -- included on this row within the diagnostic query table. One query may be represented by multiple rows. |
| 4 | `DATE_TYPE_FLAG` | DOUBLE |  |  | This field contains a representation of the type of date included in this query parameter -- range, previous dates, months, or years. |
| 5 | `END_VALUE_DT_TM` | DATETIME |  |  | This field contains the date and time of the ending query value within a specified query parameter (denoted in the PARAM_NAME field), if defined. |
| 6 | `END_VALUE_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the ending query value within a specified query parameter (denoted in the PARAM_NAME field), if defined. |
| 7 | `FREETEXT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the LONG_TEXT table that contains the free textsearch value. |
| 8 | `FREETEXT_QUERY_FLAG` | DOUBLE |  |  | This field determines whether free textsearching crosses multiple paragraphs or within a paragraph. |
| 9 | `NEGATION_IND` | DOUBLE |  |  | This field is not used at this time. |
| 10 | `PARAM_NAME` | VARCHAR(20) |  |  | This field represents the type of query criteria (collection date, diagnostic code, patient age, for example) associated with this row on the diagnostic query parameters table. |
| 11 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | This field contains the name of the parent table for the query parameter. The internal identifier is held in the BEG_VALUE_ID and END_VALUE_ID column. |
| 12 | `QUERY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal reference to codeset 14252 which contains the user-defined query name. At the time query parameters are saved, the user is required to enter a name for the query, and this name is saved to codeset 14252. |
| 13 | `QUERY_PARAM_ID` | DOUBLE | NOT NULL |  | This field contains the unique value representing the query parameters. |
| 14 | `SEQUENCE` | DOUBLE |  |  | This field contains a numeric value that is used to sequence 'query parameters' for each query (query_cd). |
| 15 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the diagnostic coding "vocabulary", if defined. Multiple vocabularies, such as SNOMED II and SNOMED III, might reside on a single system. |
| 16 | `SYNOPTIC_CCL_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the long_text table that contains the synoptic search query in CCL Format |
| 17 | `SYNOPTIC_QUERY_FLAG` | DOUBLE | NOT NULL |  | This column determines the type of synoptic query that is to be performed.0 - Search criteria not defined.1- Search current worksheets only2 - Search current and historical worksheets |
| 18 | `SYNOPTIC_XML_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This column contains the value representing the entry on the long_text table that contains the synoptic search query in XML format. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FREETEXT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `QUERY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SYNOPTIC_CCL_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SYNOPTIC_XML_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

