# MARS_REPORT

> Identifies a report and its implementation

**Description:** MARS_REPORT  
**Table type:** REFERENCE  
**Primary key:** `MARS_REPORT_ID`  
**Columns:** 13  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `MARS_REPORT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. This column is either valued with the facility or the client organization for the encounter. |
| 4 | `PARENT_REPORT_ID` | DOUBLE |  | FK→ | This field associates sub- reports to a Parent MARS Report. It is either null or a PK value of a row in this table. |
| 5 | `REPORT_IMPLEMENTATION_TXT` | VARCHAR(100) |  |  | The MARS report implementation containing the report logic. |
| 6 | `REPORT_NAME` | VARCHAR(100) | NOT NULL |  | A unique report name that identifies an XML schema document. |
| 7 | `REPORT_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Unique report name that identifies an XML schema document - upper case and alphanumeric. |
| 8 | `REPORT_TYPE_CD` | DOUBLE | NOT NULL |  | This value defines the type of MARS Report from code set 4772128. |
| 9 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PARENT_REPORT_ID` | [MARS_REPORT](MARS_REPORT.md) | `MARS_REPORT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [MARS_NODE](MARS_NODE.md) | `MARS_REPORT_ID` |
| [MARS_REPORT](MARS_REPORT.md) | `PARENT_REPORT_ID` |
| [MARS_SUITE_REPORT_RELTN](MARS_SUITE_REPORT_RELTN.md) | `MARS_REPORT_ID` |
| [MARS_SUITE_RESPONSE](MARS_SUITE_RESPONSE.md) | `MARS_REPORT_ID` |

