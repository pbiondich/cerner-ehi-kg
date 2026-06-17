# CONVERT_AUDIT_BEST_MATCH

> Stores information about best match choices made for order conversion.

**Description:** Convert Audit Best Match  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONVERT_AUDIT_BEST_MATCH_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated sequence number. |
| 2 | `CONVERT_AUDIT_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the Convert Audit Synonym table. Associates a row in this table to the CONVERT_AUDIT_SYNONYM table. |
| 3 | `FORM_CD` | DOUBLE | NOT NULL |  | The code value for the synonym's associated form |
| 4 | `PER_UNIT_STRENGTH` | VARCHAR(255) |  |  | The value of the synonym's associated strength per unit dose. |
| 5 | `PER_UNIT_STRENGTH_UNIT_CKI` | VARCHAR(255) |  |  | The unit CKI of the strength per unit dose. |
| 6 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The id of the synonym designated as the best match. |
| 7 | `TOTAL_VOLUME_DOSE` | VARCHAR(255) |  |  | The value of the total volume dose for this best match. |
| 8 | `TOTAL_VOLUME_DOSE_UNIT_CKI` | VARCHAR(255) |  |  | The unit CKI of the total volume dose. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONVERT_AUDIT_SYNONYM_ID` | [CONVERT_AUDIT_SYNONYM](CONVERT_AUDIT_SYNONYM.md) | `CONVERT_AUDIT_SYNONYM_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

