# COLLECTION_LETTER

> Store the text to be printed on the collection letter.

**Description:** Stores the text that will be printed on the collection letter.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | FK to the billing_entity table |
| 7 | `COLLECTION_GEN_DT_TM` | DATETIME |  |  | The date collection letter generation script was run. |
| 8 | `COLLECTION_LETTER_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 9 | `DUNNING_LEVEL_CD` | DOUBLE | NOT NULL |  | Code value indicating the collection state. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `LETTER_LINE1` | VARCHAR(80) |  |  | First line of text. |
| 12 | `LETTER_LINE10` | VARCHAR(80) |  |  | Tenth line of text. |
| 13 | `LETTER_LINE11` | VARCHAR(80) |  |  | Eleventh line of text |
| 14 | `LETTER_LINE12` | VARCHAR(80) |  |  | Twelveth line of text |
| 15 | `LETTER_LINE13` | VARCHAR(80) |  |  | Thirteenth line of text. |
| 16 | `LETTER_LINE14` | VARCHAR(80) |  |  | Fourteenth line of text. |
| 17 | `LETTER_LINE15` | VARCHAR(80) |  |  | Fifteenth line of text. |
| 18 | `LETTER_LINE2` | VARCHAR(80) |  |  | Second line of text. |
| 19 | `LETTER_LINE3` | VARCHAR(80) |  |  | Third line of text |
| 20 | `LETTER_LINE4` | VARCHAR(80) |  |  | Fourth line of text. |
| 21 | `LETTER_LINE5` | VARCHAR(80) |  |  | Fifth line of text. |
| 22 | `LETTER_LINE6` | VARCHAR(80) |  |  | Sixth line of text. |
| 23 | `LETTER_LINE7` | VARCHAR(80) |  |  | Seventh line of text. |
| 24 | `LETTER_LINE8` | VARCHAR(80) |  |  | Eighth line of text. |
| 25 | `LETTER_LINE9` | VARCHAR(80) |  |  | Nineth line of text. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |

