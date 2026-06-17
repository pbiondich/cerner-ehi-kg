# FHX_ACTION

> Each row on the table represents clinician's access to the patient's family member's condition record.

**Description:** FHX Action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Action taken date time |
| 2 | `ACTION_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Indicates the type of entry on the Family History personnel relation table. It can be REVIEW, CREATE, MODIFY |
| 3 | `ACTION_TZ` | DOUBLE | NOT NULL |  | Action Date Time Zone |
| 4 | `FHX_ACTION_ID` | DOUBLE | NOT NULL |  | This is the table's primary key. The unique identifier for a Family History personnel relation. Represents clinician's access to the patient's family member's condition record. |
| 5 | `FHX_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a patient Family History Activity table [FHX_ACTIVITY table]. |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FHX_ACTIVITY_ID` | [FHX_ACTIVITY](FHX_ACTIVITY.md) | `FHX_ACTIVITY_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

