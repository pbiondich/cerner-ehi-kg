# OPL_SERVICE_SETTING

> This table will store manifest agreement for clients. The OPENLink.Next Application has the capability of displaying a customizable click-through banner at logon which prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating OK. Note: "OK" was designed in OPENLink as "Accept". This table will store the flag's for this functionality and User Agreement.

**Description:** OPENLink Service Setting  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BANNER_CLOB` | LONGTEXT |  |  | A clob of text (similar to User Agreement, for usage of the application) , Displayed upon login |
| 2 | `BANNER_ENABLED_IND` | DOUBLE | NOT NULL |  | A flag which indicates if the banner(User Agreement) was enabled for the the current client group |
| 3 | `DISPLAY_BANNER_DECLINED_IND` | DOUBLE | NOT NULL |  | A flag indicating if the Banner(User Agreement) was declined |
| 4 | `OPL_SERVICE_SETTING_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the OPL_SERVICE_SETTING table. |
| 5 | `TENANT_IDENT` | VARCHAR(128) | NOT NULL |  | Tenant indicator, identifies the tenant |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

