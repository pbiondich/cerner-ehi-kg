# MLTM_BCB_ORC_MAP

> Table used to store relationships between France's UCD code and Multum Drug Identifier's for use with Millennium's order catalog

**Description:** MLTM_BCB_ORC_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BCB_DESCRIPTION` | VARCHAR(255) | NOT NULL |  | Description as provided by BCB |
| 2 | `CATALOG_CKI` | VARCHAR(25) | NOT NULL |  | CKI value as stored on the order_catalog table |
| 3 | `CIP_TXT` | VARCHAR(50) | NOT NULL |  | The CIP code as identified by BCB |
| 4 | `SYNONYM_CKI` | VARCHAR(25) | NOT NULL |  | CKI value as stored on the order_catalog_synonym table |
| 5 | `UCD_CODE` | DOUBLE | NOT NULL |  | Code as provided by BCB |
| 6 | `UCD_TXT` | VARCHAR(50) | NOT NULL |  | UCD Text |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VCIP_TXT` | VARCHAR(50) | NOT NULL |  | Virtual CIP code as identified by BCB |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

