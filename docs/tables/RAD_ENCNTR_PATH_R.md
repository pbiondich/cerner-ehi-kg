# RAD_ENCNTR_PATH_R

> Defines a template for radiology orders at a particular facility.

**Description:** RadNet Encounter Path Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Catalog Code for the radiology procedure. |
| 2 | `CKI_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | Indicates the CKI Identifier of the pattern selected to be associated with the given procedure and facility. This identifier originates in the SCR Pattern table. |
| 3 | `CKI_SOURCE` | CHAR(12) | NOT NULL |  | This column indicates the CKI Source of the pattern selected to be associated with the given procedure and facility. This identifier originates in the SCR Pattern table. |
| 4 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Marks the row as the default pathway for the facility. |
| 5 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Code for the facility in the catalog code pathway relationship. If the facility code is -1, then this pathway is for all facilities. |
| 6 | `RAD_ENCNTR_PATH_R_ID` | DOUBLE | NOT NULL |  | Unique, generated key for RAD_ENCNTR_PATH_R. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |

