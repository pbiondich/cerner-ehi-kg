# MRU_FACT_COLLECTION

> A list of up to five separate MRU facts from code set 20325 segregated by MRU Area.

**Description:** Most Recently Used Fact Collection  
**Table type:** REFERENCE  
**Primary key:** `MRU_FACT_COLLECTION_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MRU_AREA_CD` | DOUBLE | NOT NULL |  | Mru area this fact collection is associated to |
| 2 | `MRU_FACT1_CD` | DOUBLE | NOT NULL |  | Names and meanings of data items used in MRU Selections |
| 3 | `MRU_FACT2_CD` | DOUBLE | NOT NULL |  | Names and meanings of data items used in MRU Selections |
| 4 | `MRU_FACT3_CD` | DOUBLE | NOT NULL |  | Names and meanings of data items used in MRU Selections |
| 5 | `MRU_FACT4_CD` | DOUBLE | NOT NULL |  | Names and meanings of data items used in MRU Selections |
| 6 | `MRU_FACT_COLLECTION_ID` | DOUBLE | NOT NULL | PK | Primary key ID |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MRU_PRIMARY_FACT_EXTENSION](MRU_PRIMARY_FACT_EXTENSION.md) | `MRU_FACT_COLLECTION_ID` |

