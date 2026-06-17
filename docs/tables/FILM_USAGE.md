# FILM_USAGE

> The Film_Usage table contains standard information about how much film is used during a specific procedure.

**Description:** Film Usage  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The Catalog_Cd is a foreign key to the Order_Catalog table. This identifies a certain orderable procedure. |
| 2 | `FILM_SIZE_CD` | DOUBLE | NOT NULL |  | The Film_Size_Cd identifies a specific film size that is used when performing a certain procedure. |
| 3 | `FILM_TYPE_CD` | DOUBLE | NOT NULL |  | the Film_Type_Cd identifies the type of film that is used when performing a certain procedure. |
| 4 | `STANDARD_QTY` | DOUBLE |  |  | The Standard_Qty contains the standard number of films that are used when performing a certain procedure. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [SERVICE_DIRECTORY](SERVICE_DIRECTORY.md) | `CATALOG_CD` |

