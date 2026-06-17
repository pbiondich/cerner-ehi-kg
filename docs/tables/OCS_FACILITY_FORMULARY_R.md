# OCS_FACILITY_FORMULARY_R

> Used to define the formulary status of synonyms.

**Description:** Order Catalog Synonym Facility Formulary Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Identifies the facility (zero means all facilities). |
| 2 | `INPATIENT_FORMULARY_STATUS_CD` | DOUBLE | NOT NULL |  | Stores the inpatient formulary status code. |
| 3 | `OCS_FACILITY_FORMULARY_R_ID` | DOUBLE | NOT NULL |  | The unique primary key for this table. It is an internally generated sequence number. |
| 4 | `OUTPATIENT_FORMULARY_STATUS_CD` | DOUBLE | NOT NULL |  | Stores the outpatient formulary status code. |
| 5 | `RX_SYNONYM_VISIBILITY_IND` | DOUBLE | NOT NULL |  | Used to indicate prescription synonym visibility in order search. 0 - Not visible, 1 - visible. |
| 6 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the synonym. (zero means all synonyms). |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

