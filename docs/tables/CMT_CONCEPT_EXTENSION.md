# CMT_CONCEPT_EXTENSION

> Each row in the table store the information for the concept extension. Client is not allowed to modify this table.

**Description:** CMT Concept extension  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AGE1_OPERATOR` | VARCHAR(2) |  |  | Operator for age. E.g. >,<,>=,<= |
| 6 | `AGE1_UNIT_FLAG` | DOUBLE |  |  | Unit of measure for age. |
| 7 | `AGE1_VALUE` | DOUBLE |  |  | The numeric value for age. |
| 8 | `AGE2_OPERATOR` | VARCHAR(2) |  |  | Operator for age. E.g. >,<,>=,<= |
| 9 | `AGE2_UNIT_FLAG` | DOUBLE |  |  | Unit of measure for age. |
| 10 | `AGE2_VALUE` | DOUBLE |  |  | The numeric value for age. |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL | FK→ | Functional unique identifier from cmt_concept_table. |
| 13 | `CONCEPT_EXTENSION_ID` | DOUBLE | NOT NULL |  | Primary key of concept extension table |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `EXTENSION_DATA_TYPE_FLAG` | DOUBLE | NOT NULL |  | The value associated with the extension_type_meaning |
| 16 | `EXTENSION_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Value from code Set 29746 |
| 17 | `EXTENSION_VALUE` | VARCHAR(40) | NOT NULL |  | The value associated with the extension type mean |
| 18 | `GENDER_FLAG` | DOUBLE |  |  | Gender. 0 = unknown and/or do not care; 1 = male; 2 = female |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONCEPT_CKI` | [CMT_CONCEPT](CMT_CONCEPT.md) | `CONCEPT_CKI` |

