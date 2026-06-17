# CNT_CODE_VALUE_KEY

> CODE VALUE KEY

**Description:** CNT CODE VALUE KEY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDF_MEANING` | VARCHAR(12) |  |  | The actual string value for the cdf meaning. |
| 2 | `CKI` | VARCHAR(255) | NOT NULL |  | Cerner Knowledge Index for the Code Value |
| 3 | `CNT_CODE_VALUE_KEY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `CODE_SET` | DOUBLE | NOT NULL |  | The code_set for the code_value_uid |
| 5 | `CODE_VALUE` | DOUBLE | NOT NULL |  | The mapped code_value for the code_value_uid |
| 6 | `CODE_VALUE_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Code Value |
| 7 | `CODE_VALUE_UID_ALIAS` | VARCHAR(100) |  |  | ALIAS NAME FOR CODE VALUE UID |
| 8 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Concept CKI is the functional Concept Identifier; it is the codified means within Millennium to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. Composed of a source and an identifier. For example, if the concept source is "SNOMED" and the concept identifier is "123", then the CKI is "SNOMED!123". |
| 9 | `DEFINITION` | VARCHAR(100) |  |  | the definition for the code value |
| 10 | `DESCRIPTION` | VARCHAR(100) | NOT NULL |  | The description for the code value |
| 11 | `DISPLAY` | VARCHAR(40) |  |  | The display string for the code_value |
| 12 | `EVENT_SET_NAME` | VARCHAR(100) |  |  | the event set name |
| 13 | `IGNORE_IND` | DOUBLE | NOT NULL |  | field to indicate if the user has chosen NOT to match a code value from content to a code value in the domain |
| 14 | `IGNORE_USER_ID` | DOUBLE | NOT NULL | FK→ | the user who decided and chose to ignore matching a content code value with domain code value |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IGNORE_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

