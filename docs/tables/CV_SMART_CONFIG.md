# CV_SMART_CONFIG

> Stores configurations required to launch the third-party SMART apps. This table holds the configuration for tenant, facility and vendor level. Lookup hierarchy and will be as follows : First look at the facility level if one not exists then at tenant level.

**Description:** CV SMART configurations  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALL_FACILITY_IND` | DOUBLE |  |  | Set this indicator to apply SMART configuration to all the facility under the tenant. |
| 3 | `BROWSER_TFLG` | VARCHAR(250) |  |  | Contains the information about the browser on which SMART app will be launched. Currently supported values are IE_EDGE, IE_CHROMIUM. |
| 4 | `CV_SMART_CONFIG_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `FACILITY_CD` | DOUBLE |  |  | Contains the facility for which SMART app is associated. |
| 6 | `LAUNCH_URL` | VARCHAR(500) |  |  | Contains the URL of the SMART app. Example : https://smart.cerner.com/smart/ /apps/ ?PAT_PersonId={patientID}&VIS_EncntrId={EncntrId}&USR_PersonId={USRID}&username={USERNAME} |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `MIGRATION_IND` | DOUBLE |  |  | Indicates the study migration is completed when client is upgraded to the vendor agnostic viewer integrations. With this indicator set all the older studies will be able to launch on the new viewers or through SMART app of the vendor. |
| 9 | `PRODUCT_START_DT_TM` | DATETIME |  |  | Contains the date time of the usage of the new product ECG 2.0 |
| 10 | `TENANT_KEY` | VARCHAR(250) |  |  | Contains the tenant key for which SMART app is associated. |
| 11 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `VENDOR_CD` | DOUBLE |  |  | Contains the vendor code for the SMART app configured; |
| 17 | `VIEWER_TYPE_TFLG` | VARCHAR(30) |  |  | ; Type of the viewer used to launch the study. (PDF / DICOM / WEBVIEWER) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

