# INTERP_RANGE

> The result ranges defined for each discrete task assay used within an interpretation.

**Description:** Interpretation Range  
**Table type:** REFERENCE  
**Primary key:** `INTERP_RANGE_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AGE_FROM_MINUTES` | DOUBLE |  |  | The "from" age of the patient within the age range which should be used to determine the pattern of the interpretation. |
| 6 | `AGE_FROM_UNITS_CD` | DOUBLE | NOT NULL |  | The code value that represents the unit of measure for the "from age" of the patient (ex. "Minutes"). |
| 7 | `AGE_TO_MINUTES` | DOUBLE |  |  | The "to" age of the patient within the age range which should be used to determine the pattern of the interpretation. |
| 8 | `AGE_TO_UNITS_CD` | DOUBLE | NOT NULL |  | The code value that represents the unit of measure for the "to age" of the patient (ex. "Minutes"). |
| 9 | `GENDER_CD` | DOUBLE | NOT NULL |  | The code value that represents the gender of the patient, which should be used in determining the interpretation pattern. |
| 10 | `INCLUDED_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This column is the code value that represents the discrete task assay that is included in the interpretation pattern. |
| 11 | `INTERP_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | This unique number identifies the interpretation detail. |
| 12 | `INTERP_ID` | DOUBLE | NOT NULL | FK→ | This is a unique number that identifies the interpretation. |
| 13 | `INTERP_RANGE_ID` | DOUBLE | NOT NULL | PK | This unique number identifies the interpretation range. |
| 14 | `RACE_CD` | DOUBLE | NOT NULL |  | The code value that represents the race of the patient, which should be used in determining the interpretation pattern. |
| 15 | `SEQUENCE` | DOUBLE |  |  | An internal sequential number that is used to determine the sequence of the components of the interpretation pattern, which is used to organize and display the components within the Interpretation Tool. |
| 16 | `SPECIES_CD` | DOUBLE | NOT NULL |  | A code value that represents the species of the patient, which is used in determining the interpretation pattern. Allows different patterns to be defined for the same procedure, but for humans versus animals. |
| 17 | `UNKNOWN_AGE_IND` | DOUBLE |  |  | Client can specify an unknown age for their interp. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INCLUDED_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `INTERP_DETAIL_ID` | [INTERP_COMPONENT](INTERP_COMPONENT.md) | `INTERP_DETAIL_ID` |
| `INTERP_ID` | [INTERP_TASK_ASSAY](INTERP_TASK_ASSAY.md) | `INTERP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RESULT_HASH](RESULT_HASH.md) | `INTERP_RANGE_ID` |

