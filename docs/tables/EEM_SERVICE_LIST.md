# EEM_SERVICE_LIST

> EEM Service List

**Description:** EEM Service List  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CAUSE_BEG_IDENT` | VARCHAR(50) |  |  | Nomenclature Source Identifier |
| 7 | `CAUSE_BEG_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature Identifier. |
| 8 | `CAUSE_END_IDENT` | VARCHAR(50) |  |  | Nomenclature Source Identifier |
| 9 | `CAUSE_END_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature Identifier. |
| 10 | `CAUSE_INC_EXC_CD` | DOUBLE | NOT NULL |  | Include/Exclude Code |
| 11 | `CAUSE_INC_EXC_MEANING` | VARCHAR(12) |  |  | Include/Exclude Meaning |
| 12 | `CAUSE_VOCAB_CD` | DOUBLE | NOT NULL |  | Vocabulary Code |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order among the children of a group. |
| 15 | `SERVICE_LIST_ID` | DOUBLE | NOT NULL |  | Service List Identifier |
| 16 | `SERVICE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Service Type Identifier |
| 17 | `TYPE_BEG_IDENT` | VARCHAR(50) |  |  | Nomenclature Source Identifier |
| 18 | `TYPE_BEG_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature Identifier |
| 19 | `TYPE_END_IDENT` | VARCHAR(50) |  |  | Nomenclature Source Identifier |
| 20 | `TYPE_END_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature Identifier. |
| 21 | `TYPE_INC_EXC_CD` | DOUBLE | NOT NULL |  | Include/Exclude Code |
| 22 | `TYPE_INC_EXC_MEANING` | VARCHAR(12) |  |  | Include/Exclude Meaning |
| 23 | `TYPE_VOCAB_CD` | DOUBLE | NOT NULL |  | Vocabulary Code |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CAUSE_BEG_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `CAUSE_END_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `SERVICE_TYPE_ID` | [EEM_SERVICE_TYPE](EEM_SERVICE_TYPE.md) | `SERVICE_TYPE_ID` |
| `TYPE_BEG_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `TYPE_END_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

