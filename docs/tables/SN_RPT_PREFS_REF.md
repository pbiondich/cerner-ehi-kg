# SN_RPT_PREFS_REF

> This table contains all of the report preferences associated with a given report type.

**Description:** Holds Report Preference Reference information  
**Table type:** REFERENCE  
**Primary key:** `RPT_PREFS_REF_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY` | VARCHAR(200) | NOT NULL |  | The display value for the report preference. |
| 2 | `DISPLAY_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of control that will be used to collect information for this report preference. For example: a provider control, list box, text box, etc. |
| 3 | `PREFS_DATA` | VARCHAR(255) |  |  | Contains miscellaneous information about the report preferences. For example, it could contain information about which code set the preference values come from, or the actual values for this preference. |
| 4 | `PREFS_KEY` | VARCHAR(20) | NOT NULL |  | The unique key for this report preference. This is a SurgiNet defined key that is used within the report scripts to identify this preference. |
| 5 | `PREFS_KEY_A_NLS` | VARCHAR(80) |  |  | PREFS_KEY_A_NLS column |
| 6 | `PREFS_KEY_NLS` | VARCHAR(42) | NOT NULL |  | The unique key for this report preference. This is a SurgiNet defined key that is used within the report scripts to identify this preference. (NLS) |
| 7 | `PREFS_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines the type of report preference that this is. |
| 8 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | (Future functionality.) Whether this preference is required. |
| 9 | `RPT_PREFS_REF_ID` | DOUBLE | NOT NULL | PK | Report Preferences Reference ID Primary Key |
| 10 | `RPT_TYPE_CD` | DOUBLE | NOT NULL |  | Determines which report type these preferences apply to. Code Set 25069 |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_RPT_PREFS](SN_RPT_PREFS.md) | `RPT_PREFS_REF_ID` |

