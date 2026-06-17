# INFUSION_BILL_RPT_ADMIN

> To store the admin information for Infusion Billing of an patient encounter

**Description:** Infusion Billing Report Admin  
**Table type:** ACTIVITY  
**Primary key:** `INFUSION_BILL_RPT_ADMIN_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIN_BLOB` | LONGBLOB |  |  | A BLOB field containig JSON formatted data related to the infusion encounter |
| 2 | `ADMIN_END_DT_TM` | DATETIME |  |  | the date and time the medication administration ended.; |
| 3 | `ADMIN_IDENT` | VARCHAR(40) |  |  | the identifier for this administration |
| 4 | `ADMIN_START_DT_TM` | DATETIME |  |  | The medication administration was started.; |
| 5 | `DISPLAY_TXT` | VARCHAR(255) |  |  | Administration display line.; |
| 6 | `DURATION_DISPLAY_TXT` | VARCHAR(255) |  |  | Total duration display of the administration in character form |
| 7 | `DURATION_NBR` | DOUBLE |  |  | Total duration value of the administration.; |
| 8 | `IMMUNIZATION_IND` | DOUBLE | NOT NULL |  | The indicator used to determine if the order is an immunization.; |
| 9 | `INFUSED_VOLUME` | DOUBLE |  |  | The total volume of the administration across qualifying volume based ingredients |
| 10 | `INFUSION_BILL_RPT_ADMIN_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 11 | `INFUSION_BILL_RPT_ID` | DOUBLE |  | FK→ | Infusion Billing Report Identifer |
| 12 | `JSON_VRSN_TXT` | VARCHAR(20) |  |  | Stores the version of Json that is used in the BLOB column. |
| 13 | `NEEDS_REVIEW_IND` | DOUBLE | NOT NULL |  | Indicates if the administration needs to be reviewed. |
| 14 | `ORDER_ID` | DOUBLE |  | FK→ | Orders identifier; |
| 15 | `PAUSE_TIME_DISPLAY_TXT` | VARCHAR(255) |  |  | Total paused time display associated with the administration.; |
| 16 | `PAUSE_TIME_NBR` | DOUBLE |  |  | Total paused time value associated with the administration.; |
| 17 | `ROUTE_CD` | DOUBLE |  |  | The route associated with the administration.; |
| 18 | `SITE_CD` | DOUBLE |  |  | The initial site documented on an administration. |
| 19 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `VISIT_TYPE_DISPLAY_TXT` | VARCHAR(255) |  |  | The Visit type for the administration occurred within.; |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INFUSION_BILL_RPT_ID` | [INFUSION_BILL_RPT](INFUSION_BILL_RPT.md) | `INFUSION_BILL_RPT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [INFUSION_BILL_RPT_SITE_CHG](INFUSION_BILL_RPT_SITE_CHG.md) | `INFUSION_BILL_RPT_ADMIN_ID` |

