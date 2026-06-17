# SCH_DATE_LIST

> Stores all the dates associated to a scheduling date set.

**Description:** Scheduling Date List  
**Table type:** REFERENCE  
**Primary key:** `SCH_DATE_LIST_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `SCH_DATE_DT_TM` | DATETIME | NOT NULL |  | The date associated to the date set. |
| 3 | `SCH_DATE_LIST_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is internally genreated. |
| 4 | `SCH_DATE_SET_ID` | DOUBLE | NOT NULL | FK→ | The ID of the date set this date is associated to. It is the primary key of the SCH_DATE_SET table. |
| 5 | `SCH_DATE_TXT` | VARCHAR(20) | NOT NULL |  | This is the date associated to a date set but stored in a text form. This is done to ensure RDDS can correctly merge this column across domains. The value into his column should be the same as the value in SCH_DATE_DT_TM. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCH_DATE_SET_ID` | [SCH_DATE_SET](SCH_DATE_SET.md) | `SCH_DATE_SET_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCH_DATE_APPLY](SCH_DATE_APPLY.md) | `SCH_DATE_LIST_ID` |

