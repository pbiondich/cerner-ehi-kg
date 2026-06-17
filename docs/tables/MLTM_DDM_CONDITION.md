# MLTM_DDM_CONDITION

> Multum DDM Condition table

**Description:** MLTM DDM Condition  
**Table type:** REFERENCE  
**Primary key:** `CONDITION_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BODY_SYSTEM_ID` | DOUBLE | NOT NULL | FK→ | Body System ID - FK from MLTM_DDM_BODY_SYSTEM table |
| 2 | `CONDITION_ID` | DOUBLE | NOT NULL | PK | Condition ID - PK Column for this table. Also FK from MLTM_DDM_CONDITION_LIST table |
| 3 | `MEDICAL_SPECIALTY_ID` | DOUBLE | NOT NULL |  | Medical Specialty ID - FK from MLTM_MEDICAL_SPECIALTY table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BODY_SYSTEM_ID` | [MLTM_DDM_BODY_SYSTEM](MLTM_DDM_BODY_SYSTEM.md) | `BODY_SYSTEM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_DDM_CONDITION_XREF_MAP](MLTM_DDM_CONDITION_XREF_MAP.md) | `PARENT_CONDITION_ID` |

