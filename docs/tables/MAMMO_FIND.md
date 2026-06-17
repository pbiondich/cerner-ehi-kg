# MAMMO_FIND

> Mammography Case Findings

**Description:** Mammography Findings  
**Table type:** ACTIVITY  
**Primary key:** `FIND_ID`  
**Columns:** 12  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BREAST_FIND_ID` | DOUBLE | NOT NULL | FK→ | This identifies the breast findings related to the mammogram. This is a foreign key to the Mammo_Breast_Find table. |
| 2 | `FIND_ID` | DOUBLE | NOT NULL | PK | This is a meaningless number used only to uniquely identify the row. |
| 3 | `LESION_CLASS_ID` | DOUBLE | NOT NULL | FK→ | This column identifies the lesion class. This is a foreign key to the Rad_Fol_Up_Field table. |
| 4 | `PARENT_MAMMO_FIND_ID` | DOUBLE | NOT NULL | FK→ | This is used to group the different findings and store the same finding data for that group |
| 5 | `PATH_ID` | DOUBLE | NOT NULL | FK→ | This column identifies the pathology code used for ACR. This is a foreign key to the Rad_Fol_Up_Field table. |
| 6 | `SCD_TERM_ID` | DOUBLE | NOT NULL | FK→ | The designated terminology that maps to this finding. |
| 7 | `SEQUENCE` | DOUBLE |  |  | This is used to sequence the findings. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BREAST_FIND_ID` | [MAMMO_BREAST_FIND](MAMMO_BREAST_FIND.md) | `BREAST_FIND_ID` |
| `LESION_CLASS_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `PARENT_MAMMO_FIND_ID` | [MAMMO_FIND](MAMMO_FIND.md) | `FIND_ID` |
| `PATH_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `SCD_TERM_ID` | [SCD_TERM](SCD_TERM.md) | `SCD_TERM_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [MAMMO_FIND](MAMMO_FIND.md) | `PARENT_MAMMO_FIND_ID` |
| [MAMMO_FIND_DETAIL](MAMMO_FIND_DETAIL.md) | `FIND_ID` |
| [RAD_OMF_MAMMO_FIND](RAD_OMF_MAMMO_FIND.md) | `FIND_ID` |
| [RAD_OMF_MAMMO_FIND_DETAILS](RAD_OMF_MAMMO_FIND_DETAILS.md) | `FIND_ID` |

