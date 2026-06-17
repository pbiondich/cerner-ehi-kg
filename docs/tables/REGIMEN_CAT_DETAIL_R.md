# REGIMEN_CAT_DETAIL_R

> Table used to store relationships such as offsets between different components of a regimen.

**Description:** Regimen catalog detail relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OFFSET_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the offset unit (days, weeks, months). |
| 2 | `OFFSET_VALUE` | DOUBLE | NOT NULL |  | Offset quantity used to define a time offset for the relationship |
| 3 | `REGIMEN_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a REGIMEN_CATALOG. It will be used to uniquely identify a regimen. foreign key from REGIMEN_CATALOG |
| 4 | `REGIMEN_CAT_DETAIL_R_ID` | DOUBLE | NOT NULL |  | sequence name: reference_seq Unique identifier for the REGIMEN_CAT_DETAIL table. |
| 5 | `REGIMEN_CAT_DETAIL_S_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier on the REGIMEN_CAT_DETAIL table. It is an internal system assigned number. |
| 6 | `REGIMEN_CAT_DETAIL_T_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier on the REGIMEN_CAT_DETAIL table. It is an internal system assigned number. |
| 7 | `TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Identifies the type of relationship. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REGIMEN_CATALOG_ID` | [REGIMEN_CATALOG](REGIMEN_CATALOG.md) | `REGIMEN_CATALOG_ID` |
| `REGIMEN_CAT_DETAIL_S_ID` | [REGIMEN_CAT_DETAIL](REGIMEN_CAT_DETAIL.md) | `REGIMEN_CAT_DETAIL_ID` |
| `REGIMEN_CAT_DETAIL_T_ID` | [REGIMEN_CAT_DETAIL](REGIMEN_CAT_DETAIL.md) | `REGIMEN_CAT_DETAIL_ID` |

