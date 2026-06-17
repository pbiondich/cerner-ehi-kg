# EEM_BENEFIT_QUAL

> EEM Benefit Qualifier

**Description:** EEM Benefit Qualifier  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BEG_IDENT` | VARCHAR(50) |  |  | Nomenclature Source Identifier |
| 7 | `BEG_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature Identifier |
| 8 | `BENEFIT_ID` | DOUBLE | NOT NULL | FK→ | EEM BenefitIdentifier |
| 9 | `BENEFIT_QUAL_ID` | DOUBLE | NOT NULL |  | Benefit Qualifier Identifier |
| 10 | `DATA_TYPE_CD` | DOUBLE | NOT NULL |  | A unique identifier for the Data Type Code. |
| 11 | `DATE_VALUE` | DATETIME |  |  | Date Value |
| 12 | `DOUBLE_VALUE` | DOUBLE | NOT NULL |  | Double Value |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `END_IDENT` | VARCHAR(50) |  |  | Nomenclature Source Identifier |
| 15 | `END_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature Identifier |
| 16 | `FROM_UNITS` | DOUBLE | NOT NULL |  | From Units |
| 17 | `FROM_UNITS_CD` | DOUBLE | NOT NULL |  | Units Of Measure Code |
| 18 | `INC_EXC_CD` | DOUBLE | NOT NULL |  | Include/Exclude Code |
| 19 | `INC_EXC_MEANING` | VARCHAR(12) |  |  | Include/Exclude Meaning |
| 20 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Primary Key to LONG_TEXT_REFERENCE table |
| 21 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary Key of the Parent Row |
| 22 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Name of the Parent Entity |
| 23 | `QUALIFIER_CD` | DOUBLE | NOT NULL |  | Benefit Qualifier Code |
| 24 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order among the children of a group. |
| 25 | `STRING_VALUE` | VARCHAR(255) |  |  | String Value |
| 26 | `TO_UNITS` | DOUBLE | NOT NULL |  | To Units |
| 27 | `TO_UNITS_CD` | DOUBLE | NOT NULL |  | Units Of Measure Code |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 33 | `VOCABULARY_CD` | DOUBLE | NOT NULL |  | Nomenclature Vocabulary Code |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BEG_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `BENEFIT_ID` | [EEM_BENEFIT](EEM_BENEFIT.md) | `EEM_BENEFIT_ID` |
| `END_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

