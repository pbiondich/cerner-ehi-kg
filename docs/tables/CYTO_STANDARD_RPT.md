# CYTO_STANDARD_RPT

> This reference table contains the parameters (excluding the definition of result values) for each standard report created for a specific cytology report order catalog item.

**Description:** Cytology Standard Report  
**Table type:** REFERENCE  
**Primary key:** `STANDARD_RPT_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the cytology report for which the standard report has been defined. This value could be used to join to the order catalog tables, if desired. |
| 3 | `DESCRIPTION` | VARCHAR(40) |  |  | This field contains the long description of the standard report. |
| 4 | `HOT_KEY_SEQUENCE` | DOUBLE |  |  | If a hot key has been established for the standard report, this field contains a value representing the hot key sequence (first, second, third¿ tenth). |
| 5 | `SHORT_DESC` | CHAR(5) |  |  | This field contains the short description of the standard report. |
| 6 | `STANDARD_RPT_ID` | DOUBLE | NOT NULL | PK | This field uniquely defines a row (a standard report) included on the CYTO_STANDARD_REPORT table. This field would be used to join to other tables, such as the CYTO_STANDARD_REPORT_R reference table. |
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

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CYTO_SCREENING_EVENT](CYTO_SCREENING_EVENT.md) | `STANDARD_RPT_ID` |
| [CYTO_STANDARD_RPT_R](CYTO_STANDARD_RPT_R.md) | `STANDARD_RPT_ID` |

