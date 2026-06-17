# PL_PC_ORG_TAB_XREF

> Define procs on tabs for an org.

**Description:** PL PC ORG TAB XREF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Unique key from ORGANIZATION table. |
| 2 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Unique key from ORDER_CATALOG_SYNONYM table. |
| 3 | `SYNONYM_SEQ` | DOUBLE | NOT NULL |  | An into specifying the place of the synonym on the tab. |
| 4 | `TAB_DESCRIPTION` | CHAR(15) |  |  | Name of the tab. |
| 5 | `TAB_SEQ` | DOUBLE | NOT NULL |  | An into specifying the place of the tab in group. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

