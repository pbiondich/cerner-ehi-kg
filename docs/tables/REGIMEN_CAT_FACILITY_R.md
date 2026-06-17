# REGIMEN_CAT_FACILITY_R

> Facility flexing definition / Facility access for regimen catalog.

**Description:** Regimen Catalog Facility Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location to which regimen is flexed to |
| 2 | `REGIMEN_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a REGIMEN_CATALOG. It will be used to uniquely identify a regimen. foreign key from REGIMEN_CATALOG |
| 3 | `REGIMEN_CAT_FACILITY_R_ID` | DOUBLE | NOT NULL |  | sequence name: reference_seq Unique identifier for the REGIMEN_CAT_FACILITY_R table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REGIMEN_CATALOG_ID` | [REGIMEN_CATALOG](REGIMEN_CATALOG.md) | `REGIMEN_CATALOG_ID` |

