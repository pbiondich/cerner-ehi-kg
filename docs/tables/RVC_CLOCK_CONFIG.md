# RVC_CLOCK_CONFIG

> Holds configurations that will be used to calculate Revenue Cycle Clocks.

**Description:** Revenue Cycle Clock Configuration  
**Table type:** REFERENCE  
**Primary key:** `RVC_CLOCK_CONFIG_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CLOCK_TYPE_CD` | DOUBLE | NOT NULL |  | Codified value that represents type of clock ie; Days Till Letter, Guaranteed Appointment Date. |
| 7 | `DURATION` | DOUBLE | NOT NULL |  | The configured number of time units that represents the clock duration. |
| 8 | `DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | Codified value that represents the unit of duration. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 11 | `MEDICAL_SERVICE_CD` | DOUBLE | NOT NULL |  | Value of the medical service code corresponding to the clock configuration. |
| 12 | `ORIG_CLOCK_CONFIG_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the clock configurations. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 13 | `REFERRAL_PRIORITY_CD` | DOUBLE | NOT NULL |  | Value of the priority/urgency code corresponding to the clock configuration. |
| 14 | `RVC_CLOCK_CONFIG_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORIG_CLOCK_CONFIG_ID` | [RVC_CLOCK_CONFIG](RVC_CLOCK_CONFIG.md) | `RVC_CLOCK_CONFIG_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RVC_CLOCK_CONFIG](RVC_CLOCK_CONFIG.md) | `ORIG_CLOCK_CONFIG_ID` |

