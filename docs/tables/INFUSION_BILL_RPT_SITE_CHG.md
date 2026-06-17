# INFUSION_BILL_RPT_SITE_CHG

> To store the report site change information for Infusion Billing of an patient encounter

**Description:** Infusion Billing Report Site Change  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INFUSION_BILL_RPT_ADMIN_ID` | DOUBLE |  | FK→ | Infusion Billing Report admin identifier |
| 2 | `INFUSION_BILL_RPT_SITE_CHG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `SITE_CHANGE_CD` | DOUBLE |  |  | codeset that represents this site in the system.; |
| 4 | `SITE_CHANGE_PERFORMED_DT_TM` | DATETIME |  |  | The date and time the site was documented.; |
| 5 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INFUSION_BILL_RPT_ADMIN_ID` | [INFUSION_BILL_RPT_ADMIN](INFUSION_BILL_RPT_ADMIN.md) | `INFUSION_BILL_RPT_ADMIN_ID` |

