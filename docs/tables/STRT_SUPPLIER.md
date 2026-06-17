# STRT_SUPPLIER

> Stores a list of all suppliers and related information about the supplier.

**Description:** Stores a list of all suppliers of laboratory analyzers.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTACT` | VARCHAR(200) |  |  | Contains a primary contact at the laboratory analyzer supplier facility. |
| 2 | `CONTACT_FAX_NBR` | VARCHAR(33) |  |  | Contains the fax number of the primary contact at a laboratory analyzer supplier facility. |
| 3 | `CONTACT_PH_NBR` | VARCHAR(33) |  |  | Contains the phone number of a primary contact at a laboratory analyzer supplier facility. |
| 4 | `DESCRIPTION` | VARCHAR(50) |  |  | Contains the name of the laboratory analyzer supplier. |
| 5 | `STRT_SUPPLIER_ID` | DOUBLE | NOT NULL |  | Key Field. Contains the DBMS supplied unique value. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

