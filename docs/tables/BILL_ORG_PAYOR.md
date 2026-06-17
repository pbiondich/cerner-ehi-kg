# BILL_ORG_PAYOR

> Contains information about organizations that have been given a type of "client" in the organization, such as what tier group to use, and whether to generate an additional charge for the performing organization.

**Description:** Bill Organization Payor  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_ORG_TYPE_CD` | DOUBLE | NOT NULL |  | Value from 13031 that represents the type of information in this row such as "bill performing org", "clientbill", "t01bill", "tiergroup1", and "tiergroup2". |
| 7 | `BILL_ORG_TYPE_ID` | DOUBLE | NOT NULL |  | Depending on the value in bill_org_type_cd, this either indicates whether to create a charge for the performing org (1=yes, 0=no), or it is the value from 13035 that represents the tier group to use for each charge that should be generated. |
| 8 | `BILL_ORG_TYPE_IND` | DOUBLE |  |  | This field stores the indicator to determine whether the clientbill or billperforg columns in CSMiscsetup are checked. |
| 9 | `BILL_ORG_TYPE_STRING` | VARCHAR(50) |  |  | This field will contain the financial number of the bill performing org if the bill org type cd field has a value of "FINNUM" from codeset 13031 |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `INTERFACE_FILE_CD` | DOUBLE | NOT NULL |  | not used. |
| 12 | `ORGANIZATION_ID` | DOUBLE | NOT NULL |  | ID from the organization table. Only organizations of "client" type will appear on this table. |
| 13 | `ORG_PAYOR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the bill_org_payor table. It is an internal system assigned number. |
| 14 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Indicates from what table the bill_org_type_id comes, such as code_value. |
| 15 | `PRIORITY` | DOUBLE |  |  | not used |
| 16 | `TIER_GROUP_CD` | DOUBLE | NOT NULL |  | not used |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

