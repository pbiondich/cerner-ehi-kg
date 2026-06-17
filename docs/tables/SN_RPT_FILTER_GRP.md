# SN_RPT_FILTER_GRP

> This table holds the filter groups for a report. Each filter group will hold: printing file properties, filters, output destinations, and privileges.

**Description:** This table holds the filter groups for a report.  
**Table type:** REFERENCE  
**Primary key:** `RPT_FILTER_GRP_ID`  
**Columns:** 19  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPEND_IND` | DOUBLE | NOT NULL |  | Indicates if appending existing print file is desired (0 - False, 1 - True). |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was initially inserted. |
| 4 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 5 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that created the row. |
| 6 | `DIR_NAME` | VARCHAR(100) |  |  | Specifies the name of the logical or the full directory path where the print file will be generated. |
| 7 | `DISPLAY` | VARCHAR(60) | NOT NULL |  | The display value for this filter group. |
| 8 | `FILE_FORMAT` | DOUBLE | NOT NULL |  | Specifies the format of the print file (0 - Postscript, 1 - ASCII, 2 - CSV). |
| 9 | `FILE_NAME` | VARCHAR(50) |  |  | Specifies the name of the print file. |
| 10 | `OWNER_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) assigned to own the filter group. |
| 11 | `PAGE_BREAK_IND` | DOUBLE | NOT NULL |  | Indicates if page break is desired in the print file (0 - False, 1 - True). |
| 12 | `RPT_FILTER_GRP_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 13 | `RPT_ID` | DOUBLE | NOT NULL |  | This is a foreign key into the SN_RPT table to indicate which report this filter group belongs. |
| 14 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates what type of applications this filter group applies to. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `OWNER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SN_RPT_DEST](SN_RPT_DEST.md) | `RPT_FILTER_GRP_ID` |
| [SN_RPT_FILTER](SN_RPT_FILTER.md) | `RPT_FILTER_GRP_ID` |
| [SN_RPT_PREFS](SN_RPT_PREFS.md) | `RPT_FILTER_GRP_ID` |

