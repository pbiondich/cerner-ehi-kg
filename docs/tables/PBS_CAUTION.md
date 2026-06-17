# PBS_CAUTION

> Australian Pharmaceutical Benefits Schedule Caution Text

**Description:** PBS_CAUTION  
**Table type:** REFERENCE  
**Primary key:** `PBS_CAUTION_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CAUTION_IDENT` | DOUBLE | NOT NULL |  | PBS XML caution id |
| 2 | `CAUTION_TEXT` | LONGTEXT |  |  | Caution Text - LONG text format |
| 3 | `PBS_CAUTION_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the PBS_CAUTION table. It is an internal system assigned number. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PBS_CAUTION_RELTN](PBS_CAUTION_RELTN.md) | `PBS_CAUTION_ID` |

