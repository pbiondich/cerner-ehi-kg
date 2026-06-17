# PULSE_GEN_LEAD

> Contains information about a lead for a pulse generator device, such as the model, serial number, manufacturer, and physical location of the lead.

**Description:** Pulse Generator Lead  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONNECTION_CD` | DOUBLE | NOT NULL |  | The physical connection status of the lead, either connected or abandoned |
| 2 | `ELECTRODE_POLARITY_CD` | DOUBLE | NOT NULL |  | The number of electrodes on the lead |
| 3 | `IMPLANT_DT_TM` | DATETIME |  |  | The implant date of the lead |
| 4 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The fixation location of the lead, usually indicating a chamber of the heart |
| 5 | `LOCATION_DETAIL1_CD` | DOUBLE | NOT NULL |  | Further details describing the location |
| 6 | `LOCATION_DETAIL2_CD` | DOUBLE | NOT NULL |  | Further details describing the location |
| 7 | `LOCATION_DETAIL3_CD` | DOUBLE | NOT NULL |  | Further details describing the location |
| 8 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | The manufacturer of the lead |
| 9 | `MODEL_IDENT` | VARCHAR(50) |  |  | The model of the lead |
| 10 | `PULSE_GEN_ID` | DOUBLE | NOT NULL | FK→ | The pulse generator associated with this lead |
| 11 | `PULSE_GEN_LEAD_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 12 | `REMOVAL_DT_TM` | DATETIME |  |  | The removal date of the lead |
| 13 | `SERIAL_TXT` | VARCHAR(40) |  |  | The serial number of the lead |
| 14 | `SPECIAL_FUNCTION` | VARCHAR(20) |  |  | A description of any special attribute or function of the lead |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PULSE_GEN_ID` | [PULSE_GEN](PULSE_GEN.md) | `PULSE_GEN_ID` |

