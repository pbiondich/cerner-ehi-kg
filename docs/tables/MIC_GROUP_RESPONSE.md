# MIC_GROUP_RESPONSE

> This table contains the information regarding group report responses defined for a microbiology orderable procedure and service resource.

**Description:** Microbiology Group Response Criteria  
**Table type:** REFERENCE  
**Primary key:** `GROUP_RESPONSE_ID`  
**Columns:** 17  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CARRY_FORWARD_IND` | DOUBLE | NOT NULL |  | This column represents whether group responses can be carry forwarded in successive reports or not. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code value assigned to the procedure as defined in the DCPtools.exe application. Ordered procedure code values are stored on code set 200 Order Catalog. |
| 4 | `GROUP_DESCRIPTION` | VARCHAR(60) |  |  | Description of the group response |
| 5 | `GROUP_DISPLAY` | VARCHAR(40) |  |  | Display of the group response |
| 6 | `GROUP_RESPONSE_ID` | DOUBLE | NOT NULL | PK | This field identifies a unique value for each group response defined for an orderable procedure/service resource combination. |
| 7 | `GRP_RESPONSE_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of the group response code associated with the procedure and service resource. |
| 8 | `POSITIVE_IND` | DOUBLE |  |  | This field indicates whether the group response is to be considered positive or negative at the group response level. Valid value include: 0 = Negative 1 = Positive |
| 9 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the service resource to which group responses are defined.Service resources are defined on code set 221. |
| 10 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of the source to which group responses are defined. Sources are defined on code set 2052, 1150 and 1151. |
| 11 | `STATISTICS_IND` | DOUBLE |  |  | Indicator to determine if the response should be sent to archive for statistical purposes. Marked with a 1 if detail responses should be sent or a 2 on the first detail if the group should be sent |
| 12 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the report associated with the group response. Reports are defined on code set 1000, Microbiology Reports. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `TASK_ASSAY_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MIC_GROUP_RESPONSE_MBR](MIC_GROUP_RESPONSE_MBR.md) | `GROUP_RESPONSE_ID` |
| [MIC_REF_ANG_REPORT](MIC_REF_ANG_REPORT.md) | `GROUP_RESPONSE_ID` |
| [MIC_STAT_REPORT_RESPONSE](MIC_STAT_REPORT_RESPONSE.md) | `GROUP_RESPONSE_ID` |

