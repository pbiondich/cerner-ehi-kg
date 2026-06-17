# EKS_TEMPLATE

> Records in this table define the overall characteristics of EKS module templates. Templates are the basic component used to build EKS modules.

**Description:** EKS template header table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_FLAG` | CHAR(1) | NOT NULL |  | The active flag denotes whether the template and its version represented by this record is active or not. If active, this flag will be 'A', and if inactive,the flag will be 'I'. |
| 2 | `ALWAYS_TRUE_IND` | DOUBLE | NOT NULL |  | The indicator of the return value (retval) for template. 0 means this template does not always return true. 1 means this template always return true. |
| 3 | `DESCRIPTION` | VARCHAR(255) |  |  | The description of the template represented by this template header record. |
| 4 | `EDITOR_DEF` | VARCHAR(2000) |  |  | The template's text that is viewable in the EKM editor. This text contains embedded parameter names. |
| 5 | `EKM_DEF` | LONGTEXT |  |  | This is the subroutine text that will be compiled by the module editor using CCL when the template is pulled into a module and saved as part of the module. |
| 6 | `KEYWORD` | VARCHAR(30) |  |  | is used for display purposes on the frontend and will be put in a sortable column of a list box. |
| 7 | `NUM_PARAMS` | DOUBLE |  |  | Number of parameters used by the template. Parameters are variables specified by the module builder when a template is used (instantiated) in a module. |
| 8 | `RECOMMEND_FLAG` | DOUBLE | NOT NULL |  | RECOMMEND_FLAG can have one of 3 values. 0 = Recommend; 1 = Use with Caution; 2 = Not Recommended |
| 9 | `TEMPLATE_NAME` | CHAR(30) | NOT NULL |  | The name of the template represented by this header record. |
| 10 | `TEMPLATE_TYPE` | CHAR(1) |  |  | The type of the template. Templates are defined to be usable in a specified section of the EXPERT module. The type field denotes which portion of the module this template can be used in. Possible values are: 'L' - LOGIC, 'A'- ACTION, 'D'-DATA, and 'E' - EVOKE. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `VERSION` | CHAR(10) | NOT NULL |  | Each time a template is saved, it's version number is incremented and the newest version is made active. This field contains the version number. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

