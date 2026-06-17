# EEM_ABN_DATA

> EEM ABN Data

**Description:** Hold additional attributes for an ABN code pair  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 36

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_ATTR_ID` | DOUBLE | NOT NULL |  | ABN Attribute Identifier |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ATTR_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Attribute Type Code |
| 7 | `ATTR_TYPE_MEANING` | VARCHAR(12) |  |  | Attribute Type Meaning |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BEG_IDENTIFIER` | VARCHAR(50) |  |  | This field contains the begin SOURCE_IDENTIFIER for a range of NOMENCLATURE values. |
| 10 | `BEG_SEQ` | DOUBLE | NOT NULL |  | Denote the first import sequence to contain the record |
| 11 | `COMP_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Comparison Type Code |
| 12 | `COMP_TYPE_MEANING` | VARCHAR(12) |  |  | Comparison Type Meaning |
| 13 | `DATA_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the Data Type Code. |
| 14 | `DATA_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Data Type. |
| 15 | `DATE_VALUE` | DATETIME |  |  | Date/Time Value |
| 16 | `DOUBLE_VALUE` | DOUBLE |  |  | Double Value (any numerical value) |
| 17 | `EEM_FILE_ID` | DOUBLE | NOT NULL | FK→ | EEM Content File Identifier value |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `END_IDENTIFIER` | VARCHAR(50) |  |  | This field contains the ;last SOURCE_IDENTIFIER for a range of NOMENCLATURE values. |
| 20 | `END_SEQ` | DOUBLE | NOT NULL |  | Denote the last content file to contain the record. |
| 21 | `KEY_FIELD` | DOUBLE | NOT NULL |  | This field provides a link between the code pair in EEM_ABN_RULE and the additional attributes stored in EEM_ABN_DATA. |
| 22 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Id of long text row containing note |
| 23 | `PARENT_ID` | DOUBLE | NOT NULL |  | Parent Identifier |
| 24 | `PARENT_MEANING` | VARCHAR(12) |  |  | Parent Meaning |
| 25 | `PARENT_TABLE` | VARCHAR(30) |  |  | Parent Table |
| 26 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order among the children of a group. |
| 27 | `STRING_VALUE` | VARCHAR(255) |  |  | String Value |
| 28 | `UNITS_CD` | DOUBLE | NOT NULL | FK→ | Denotes the Units of Measure |
| 29 | `UNITS_MEANING` | VARCHAR(12) |  |  | Denotes the Units of Measure |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 35 | `VOCABULARY_CD` | DOUBLE | NOT NULL | FK→ | Nomenclature Vocabulary Code |
| 36 | `VOCABULARY_MEANING` | VARCHAR(12) |  |  | Nomenclature Vocabulary Meaning |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ATTR_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `COMP_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DATA_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `EEM_FILE_ID` | [EEM_FILE](EEM_FILE.md) | `EEM_FILE_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `VOCABULARY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

