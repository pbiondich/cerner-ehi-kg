# HE_OBJECT

> Store serialized health expert objects for future reuse. These object will include knowledge base versions, resolved fact patterns, and other objects used to optimize processing by the health expert jobs.

**Description:** HE_OBJECT  
**Table type:** ACTIVITY  
**Primary key:** `HE_OBJECT_ID`  
**Columns:** 7  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HE_OBJECT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 2 | `OBJECT_NAME` | VARCHAR(250) | NOT NULL |  | Uniquely identifies the type of health expert object being serialized. The object name provides a way to group together object entries under a single name (type). |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HE_OBJECT_ENTRY](HE_OBJECT_ENTRY.md) | `HE_OBJECT_ID` |

