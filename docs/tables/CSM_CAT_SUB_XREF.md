# CSM_CAT_SUB_XREF

> This is the request table for CSM.

**Description:** A combination of categories and subcategories will make a request.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CSM_CALLBACK_IND` | DOUBLE |  |  | Field to allow user to categorize request as a callback/non-callback type. |
| 3 | `CSM_CAT_ID` | DOUBLE | NOT NULL | FK→ | Id of the category associated with this request. |
| 4 | `CSM_SUB_CAT_ID` | DOUBLE | NOT NULL | FK→ | Id for the sub category associated with this request. |
| 5 | `REQ_AV_FLAG` | DOUBLE |  |  | Auto-Verify flag. 0 - on |
| 6 | `REQ_MNEMONIC` | CHAR(10) |  |  | A mnemonic given to the request to make ordering easier for the user. |
| 7 | `REQ_PHONE_FLAG` | DOUBLE | NOT NULL |  | 0 = Patient Location, 1 = Chart Copy-to Location |
| 8 | `REQ_PURGE_DAYS` | DOUBLE |  |  | Number of days to retain request data on the system. |
| 9 | `REQ_SECURITY` | DOUBLE |  |  | Reserved for future use. |
| 10 | `REQ_TEMPL_ID` | DOUBLE | NOT NULL | FK→ | The unique id of the template to be used for inputting data on the request. |
| 11 | `RESL_TEMPL_ID` | DOUBLE | NOT NULL | FK→ | The unique id for the template to input data on lthe result of the request. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CSM_CAT_ID` | [CSM_CATEGORIES](CSM_CATEGORIES.md) | `CSM_CAT_ID` |
| `CSM_SUB_CAT_ID` | [CSM_SUB_CATEGORIES](CSM_SUB_CATEGORIES.md) | `CSM_SUB_CAT_ID` |
| `REQ_TEMPL_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |
| `RESL_TEMPL_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |

