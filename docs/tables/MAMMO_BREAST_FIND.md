# MAMMO_BREAST_FIND

> Mammography case Breast findings

**Description:** Mammography Breast Finding  
**Table type:** ACTIVITY  
**Primary key:** `BREAST_FIND_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BREAST_COMP_ID` | DOUBLE | NOT NULL | FK→ | This identifies the breast composition. This is a foreign key to the Rad_Fol_Up_Field table. |
| 2 | `BREAST_FIND_ID` | DOUBLE | NOT NULL | PK | This is a meaningless number that is used only to uniquely identify the row. |
| 3 | `CHANGES_ID` | DOUBLE | NOT NULL | FK→ | Not Used |
| 4 | `PARENT_BREAST_FIND_ID` | DOUBLE | NOT NULL | FK→ | Parent study's breast find id when the procedures are associated |
| 5 | `PRIOR_SURG_FOL_UP_ID` | DOUBLE | NOT NULL | FK→ | Not Used |
| 6 | `SIDE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the breast(s) that the finding is related to. |
| 7 | `STUDY_ID` | DOUBLE | NOT NULL | FK→ | This identifies the study that the findings are for. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BREAST_COMP_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `CHANGES_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `PARENT_BREAST_FIND_ID` | [MAMMO_BREAST_FIND](MAMMO_BREAST_FIND.md) | `BREAST_FIND_ID` |
| `PRIOR_SURG_FOL_UP_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `SIDE_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `STUDY_ID` | [MAMMO_STUDY](MAMMO_STUDY.md) | `STUDY_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MAMMO_BREAST_FIND](MAMMO_BREAST_FIND.md) | `PARENT_BREAST_FIND_ID` |
| [MAMMO_FIND](MAMMO_FIND.md) | `BREAST_FIND_ID` |

