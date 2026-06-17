# CMT_SUBSET

> The subset table serves as grouper to concepts to support the needs of different specialties or organizations.

**Description:** CMT SUBSET  
**Table type:** REFERENCE  
**Primary key:** `SUBSET_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SUBSET_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the subset |
| 2 | `SUBSET_MEAN` | VARCHAR(12) |  |  | The unique name that represent the subset. |
| 3 | `SUBSET_NAME` | VARCHAR(255) |  |  | A name that describes the purpose or usage of this subset. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CMT_SUBSET_MEMBER](CMT_SUBSET_MEMBER.md) | `CHILD_SUBSET_ID` |
| [CMT_SUBSET_MEMBER](CMT_SUBSET_MEMBER.md) | `SUBSET_ID` |

