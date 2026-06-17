# CONVERT_AUDIT_SYNONYM

> Stores information about requested synonyms for order conversion.

**Description:** Convert Audit Synonym  
**Table type:** ACTIVITY  
**Primary key:** `CONVERT_AUDIT_SYNONYM_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONVERT_AUDIT_SYNONYM_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally generated sequence number. |
| 2 | `CONVERT_AUDIT_TRANSACTION_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the Convert Audit Transaction table. Associates synonyms to transactions. |
| 3 | `DOSE_VALIDATION_ERROR_IND` | DOUBLE | NOT NULL |  | Indicates if a dose validation error was encountered. |
| 4 | `FORM_VALIDATION_ERROR_IND` | DOUBLE | NOT NULL |  | Indicates if a form validation error was encountered. |
| 5 | `FREETEXT_DOSE_IND` | DOUBLE | NOT NULL |  | Indicates if a free text dose was supplied. |
| 6 | `INFERRED_FORM_CD` | DOUBLE | NOT NULL |  | The form code inferred from a product synonym. |
| 7 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The id of the order to which the synonym is associated. |
| 8 | `ROUTE_CD` | DOUBLE | NOT NULL |  | The route code supplied for conversion. |
| 9 | `SUPPLIED_FORM_CD` | DOUBLE | NOT NULL |  | The form code supplied for conversion. |
| 10 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The id of the requested synonym that should be converted. |
| 11 | `TOTAL_STRENGTH_DOSE` | VARCHAR(255) |  |  | The value of the total strength dose requested. |
| 12 | `TOTAL_STRENGTH_DOSE_UNIT_CKI` | VARCHAR(255) |  |  | The unit CKI of the total strength dose. |
| 13 | `TOTAL_VOLUME_DOSE` | VARCHAR(255) |  |  | The value of the total volume dose requested. |
| 14 | `TOTAL_VOLUME_DOSE_UNIT_CKI` | VARCHAR(255) |  |  | The unit CKI of the total volume dose. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONVERT_AUDIT_TRANSACTION_ID` | [CONVERT_AUDIT_TRANSACTION](CONVERT_AUDIT_TRANSACTION.md) | `CONVERT_AUDIT_TRANSACTION_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CONVERT_AUDIT_BEST_MATCH](CONVERT_AUDIT_BEST_MATCH.md) | `CONVERT_AUDIT_SYNONYM_ID` |

