# FREQUENCY_SCHEDULE

> The schedule details for the frequency (i.e. TOD, DOW, Interval, etc.)

**Description:** FREQUENCY SCHEDULE  
**Table type:** REFERENCE  
**Primary key:** `FREQUENCY_ID`  
**Columns:** 32  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Used for flexing frequencies by department/activity. Default is activity_type_cd of 0, A given frequency will have 1 or more associated activity type codes it is valid for, each schedule will be specific to 1 activity_type |
| 3 | `CRITICAL_UPDT_DT_TM` | DATETIME |  |  | The date and time when the critical modify action was performed. |
| 4 | `CRITICAL_UPD_ID` | DOUBLE | NOT NULL | FK→ | The user id of the person who performed the critical modify action. |
| 5 | `DEFAULT_PAR_VAL` | DOUBLE |  |  | A par value to be defaulted during Order Entry when this frequency is ordered and the order has been specified as PRN. Order catalog-level par values will override this. |
| 6 | `DESCRIPTION` | VARCHAR(100) |  |  | Provides a user-defined description for the frequency schedule. |
| 7 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Applies to ad hoc frequencies only. Used to maintain a record of when a given schedule was in effect for an order. |
| 8 | `FACILITY_CD` | DOUBLE | NOT NULL |  | This column is used for flexing schedules by facility. |
| 9 | `FIRST_DOSE_METHOD` | DOUBLE |  |  | Defines the method used to calculate the start date/time for the order. |
| 10 | `FIRST_DOSE_RANGE` | DOUBLE |  |  | Defines the range to calculate the start date/time when the first_dose_method of 3 is selected. The range is expressed as defined by the first_dose_range_unit. |
| 11 | `FIRST_DOSE_RANGE_UNITS` | DOUBLE |  |  | Defines the time unit of the first_dose_range, applicable only if first_dose_method of 3. |
| 12 | `FREQUENCY_CD` | DOUBLE | NOT NULL |  | The parent frequency code value |
| 13 | `FREQUENCY_ID` | DOUBLE | NOT NULL | PK | A specific schedule for the parent frequency |
| 14 | `FREQUENCY_TYPE` | DOUBLE |  |  | Defines what kind of schedule this frequency is using. 1 = time of day, 2 = day of week, 3 = interval, 4 = onetime only, 5 = no specific time |
| 15 | `FREQ_QUALIFIER` | DOUBLE | NOT NULL |  | Primary Key. Defines the domain of ordering attributes which point to the appropriate schedule for a specific order. Frequency_qualifier = 16 represents custom frequencies. |
| 16 | `INSTANCE` | DOUBLE | NOT NULL |  | Will be stored as an order detail for a given order. Only applies to ad hoc frequencies, and is incremented every time the schedule for the ad hoc is modified. Will allow a record of changes to the scheduled to be maintained |
| 17 | `INTERVAL` | DOUBLE |  |  | Defines the interval of the frequency scheduled defined as interval_units. Only applicable to frequency_type of 3. |
| 18 | `INTERVAL_UNITS` | DOUBLE |  |  | Defines the time unit of the interval. Only applicable to frequency_type of 3. |
| 19 | `MAX_EVENT_PER_DAY` | DOUBLE |  |  | Maximum number of events to be given in one day. NOTE: PharmNet will use this field only with Type 5 frequencies for purposes of Dosage Range Management rules or other rules based on doses per day |
| 20 | `MIN_EVENT_PER_DAY` | DOUBLE |  |  | Minimum number of events (e.g. Dispenses, administrations, etc.) to be counted, charted, etc. per day. NOTE: PharmNet will use this field only with Type 5 frequencies for purposes of Dosage Range Management rules or other rules based on doses per day. |
| 21 | `MIN_INTERVAL_NBR` | DOUBLE | NOT NULL |  | The suggested minimum elapsed time between administrations. |
| 22 | `MIN_INTERVAL_UNIT_CD` | DOUBLE | NOT NULL |  | The unit value for the minimum interval number (i.e. day(s), minute(s), second(s), etc.) |
| 23 | `PARENT_ENTITY` | CHAR(32) |  |  | These act as pointers to the flexing agent. Frequencies are flexed by the following: Physician, Location, Location Group, Orderable, Therapeutic Class. In the case of an Ad-hoc frequency, this will be ORDERS. |
| 24 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent entity id for merge. Root entity will vary depending on type of frequencies. Qualifiers 10 & 8 will refer to the code_value table qualifier 4 to the order_catalog Qualifier 6 to the alt_sel_cat table Qualifier 12 to prsnl table Qualifier 16 to the orders table |
| 25 | `PRN_DEFAULT_IND` | DOUBLE |  |  | PRN Indicator |
| 26 | `ROUND_TO` | DOUBLE |  |  | Defines the rounding in minutes when the first_dose_ method of 0 is selected. |
| 27 | `RX_TOD_DOW_ID` | DOUBLE | NOT NULL | FK→ | Time of Day and Day of Week combination that this frequency occurs. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `CRITICAL_UPD_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RX_TOD_DOW_ID` | [RX_TOD_DOW](RX_TOD_DOW.md) | `RX_TOD_DOW_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ORDERS](ORDERS.md) | `FREQUENCY_ID` |
| [ORDER_ACTION](ORDER_ACTION.md) | `FREQUENCY_ID` |
| [ORDER_DISPENSE](ORDER_DISPENSE.md) | `FREQUENCY_ID` |

