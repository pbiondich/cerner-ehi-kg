# LH_AMB_REPORT_PARAM

> This table contains the list of parameters selected for MU EP Report through lh_amb_report_param prompt.

**Description:** LH_AMB_REPORT_PARAM  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EXTRACT_DT_TM` | DATETIME | NOT NULL |  | This column stores the Reporting Start Date & Time |
| 3 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | List of EP's br_eligible_provider_ids |
| 4 | `CMS_PROGRAM` | VARCHAR(50) |  |  | Indicates the cms program to be run (NQF, PQRS, CPC¿) |
| 5 | `CUST_END_DT_TM` | DATETIME | NOT NULL |  | This column stores the Custom Reporting Period End Date & Time |
| 6 | `CUST_START_DT_TM` | DATETIME | NOT NULL |  | This column stores the Custom Reporting Period Start Date & Time |
| 7 | `END_EXTRACT_DT_TM` | DATETIME | NOT NULL |  | Reporting End Date & Time |
| 8 | `EP_NAME_FILTER` | VARCHAR(10) |  |  | Eligible Providers' Name Filter |
| 9 | `LH_AMB_REPORT_PARAM_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_AMB_REPORT_PARAM table. |
| 10 | `LH_CQM_REPORT_TYPE_TFLG` | VARCHAR(5) |  |  | Determines the reporting type as MIPs or MVPs. |
| 11 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 12 | `MEASURE_NAME` | VARCHAR(2000) |  |  | List of measures, the MU Report would be executed |
| 13 | `OPT_INITIATIVE` | VARCHAR(25) |  |  | This column stores the 'Reporting Time Frame' |
| 14 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | List of Organization_ID, for which the MU Report would be executed |
| 15 | `OUTPUT_DEVICE` | VARCHAR(50) | NOT NULL |  | OUTPUT_DEVICE for future use. which can be used by the client to give the output csv file name.. By default this will be 'MINE' for now. |
| 16 | `REPORT_BY` | VARCHAR(50) | NOT NULL |  | Indicates the run mode of the report. Individual provider mode ("INDV"), group mode ("GPRO") or "CPC" mode. |
| 17 | `REPORT_FORMAT` | VARCHAR(25) |  |  | Stores format of the report to be generated. Possible Value: PS,CSV. |
| 18 | `RUN_SUMMARY_REPORT` | DOUBLE | NOT NULL |  | 0 = Run Detailed Report; 1 = Run summary report |
| 19 | `STAGE1A_DT_TM` | DATETIME | NOT NULL |  | This column stores the 90-Day Reporting Period Start Date & Time |
| 20 | `STAGE1B_YEAR` | DOUBLE | NOT NULL |  | This column stores 12 month Reporting Period's Year |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

