# AP_PREFIX

> This reference table contains the basic parameters for pathology case prefixes. A prefix is a required component of every pathology case number, and is sequenced immediately following the accession site code value.

**Description:** AP Prefix  
**Table type:** REFERENCE  
**Primary key:** `PREFIX_ID`  
**Columns:** 26  
**Referenced by:** 13 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_FORMAT_CD` | DOUBLE | NOT NULL | FK→ | This field contains the reference to the general (common) parameters associated with the prefix value. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `CASE_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains a flag value documenting the generic categorization of case type (surgical pathology, gyn cytology, non-gyn cytology, autopsy, for example) that is associated with the case prefix value. |
| 4 | `CONSULT_IND` | DOUBLE |  |  | This field is not used at this time. |
| 5 | `DEFAULT_PROC_CATALOG_CD` | DOUBLE | NOT NULL |  | This field contains a reference to the order catalog or processing group item that has been designated as the default processing task for the case prefix value. |
| 6 | `DIAG_CODING_VOCABULARY_CD` | DOUBLE | NOT NULL |  | This field contains the internal code representing the diagnostic coding vocabulary assigned to the pathology accession prefix. One prefix can be associated with only one vocabulary (such as SNOMED International). |
| 7 | `GROSS_TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 8 | `GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field contains the accession group code value that is associated with the case prefix value. The group represents a set of available case numbers. One or more prefixes may be associated with a single group value. |
| 9 | `IMAGING_INTERFACE_IND` | DOUBLE | NOT NULL |  | This field indicates whether a case will be interfaced to a foreign Imaging system. |
| 10 | `IMAGING_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The service resource code used to interface to an imaging system. |
| 11 | `INITIATE_PROTOCOL_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not default processing tasks (based on prefix, specimen, and/or pathologist) should be automatically ordered upon case initiation, or should be defaulted in the task order entry application. |
| 12 | `INTERFACE_FLAG` | DOUBLE | NOT NULL |  | This field indicates whether a case will be interfaced to a foreign tracking system. 0 - Not interfaced; 1 - Interfaced to Tracking System |
| 13 | `ORDER_CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains a reference to the order catalog item that has been designated as the prefix order catalog item. This item is automatically ordered once for each specimen received for the case. |
| 14 | `PREFIX_DESC` | VARCHAR(40) |  |  | This field contains the description of the prefix value. |
| 15 | `PREFIX_ID` | DOUBLE | NOT NULL | PK | This field uniquely defines a row included on the AP_PREFIX table (the prefix). This field would be used to join to other tables, such as the PREFIX_REPORT_R and AP_PREFIX_AUTO_TASK reference tables. |
| 16 | `PREFIX_NAME` | CHAR(2) |  |  | This field contains the short name (mnemonic) representing the prefix value. |
| 17 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The default service resource associated to the prefix. |
| 18 | `SITE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to identify the site code value associated with the prefix value. |
| 19 | `SPECIMEN_GROUPING_CD` | DOUBLE | NOT NULL |  | This field contains the reference to the specimen grouping associated with the prefix value (if present). Specimen groupings are defined on codeset 1312, and the specimens associated with the grouping are stored on the SPECIMEN_GROUPING_R table. |
| 20 | `TRACKING_SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The service resource code used to interface to a tracking system |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `WORKSHEET_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code of the cytology screening worksheet template associated with the accession prefix. This value could be used to join to the WP_TEMPLATE table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_FORMAT_CD` | [ACCESSION_ASSIGN_XREF](ACCESSION_ASSIGN_XREF.md) | `ACCESSION_FORMAT_CD` |
| `GROUP_ID` | [PREFIX_GROUP](PREFIX_GROUP.md) | `GROUP_ID` |
| `ORDER_CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `SITE_CD` | [ACCESSION_ASSIGN_XREF](ACCESSION_ASSIGN_XREF.md) | `SITE_PREFIX_CD` |
| `WORKSHEET_TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |

## Referenced by (13)

| From table | Column |
|------------|--------|
| [AP_DIAG_RPT_REVIEW](AP_DIAG_RPT_REVIEW.md) | `PREFIX_ID` |
| [AP_INV_RETENTION](AP_INV_RETENTION.md) | `PREFIX_ID` |
| [AP_PREFIX_ACCN_TEMPLATE_R](AP_PREFIX_ACCN_TEMPLATE_R.md) | `PREFIX_ID` |
| [AP_PREFIX_AUTO_TASK](AP_PREFIX_AUTO_TASK.md) | `PREFIX_ID` |
| [AP_PREFIX_DIAG_AXIS](AP_PREFIX_DIAG_AXIS.md) | `PREFIX_ID` |
| [AP_PREFIX_DIAG_SMRY](AP_PREFIX_DIAG_SMRY.md) | `PREFIX_ID` |
| [AP_PREFIX_PROC_GRP_R](AP_PREFIX_PROC_GRP_R.md) | `PREFIX_ID` |
| [AP_PREFIX_STATION_R](AP_PREFIX_STATION_R.md) | `PREFIX_ID` |
| [AP_PREFIX_TAG_GROUP_R](AP_PREFIX_TAG_GROUP_R.md) | `PREFIX_ID` |
| [AP_PREFIX_TASK_R](AP_PREFIX_TASK_R.md) | `PREFIX_ID` |
| [AP_SYNOPTIC_SPEC_PREFIX_R](AP_SYNOPTIC_SPEC_PREFIX_R.md) | `PREFIX_ID` |
| [PREFIX_REPORT_R](PREFIX_REPORT_R.md) | `PREFIX_ID` |
| [PREFIX_RPT_FONT_INFO](PREFIX_RPT_FONT_INFO.md) | `PREFIX_ID` |

