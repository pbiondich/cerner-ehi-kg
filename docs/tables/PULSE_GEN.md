# PULSE_GEN

> Contains basic information about a pulse generator device (e.g. an ICD or Pacemaker) implanted into a person

**Description:** Pulse Generator  
**Table type:** ACTIVITY  
**Primary key:** `PULSE_GEN_ID`  
**Columns:** 21  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSOCIATION_DT_TM` | DATETIME |  |  | The date and time this pulse generator was associated to a person |
| 2 | `ASSOC_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who associated this device |
| 3 | `IMPLANTER_CONTACT_INFO` | VARCHAR(100) |  |  | The contact information of the physician that implanted the pulse generator |
| 4 | `IMPLANTER_NAME` | VARCHAR(50) |  |  | The name of the physician that implanted the pulse generator |
| 5 | `IMPLANTING_FACILITY_NAME` | VARCHAR(100) |  |  | The facility (clinic/hospital) where the pulse generator was implanted |
| 6 | `IMPLANT_DT_TM` | DATETIME |  |  | The implant date of the pulse generator |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | The manufacturer of the pulse generator |
| 9 | `MODEL_IDENT` | VARCHAR(50) |  |  | The model identifier of the pulse generator |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person associated with this pulse generator |
| 11 | `PULSE_GEN_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 12 | `PULSE_GEN_PID_ID` | DOUBLE | NOT NULL | FK→ | ID for the PID informaton from an external system.The external database's information won't match up exactly with our PERSON table, we need to keep track of this information somehow. These new columns will eventually be used to assist a cardiology tech in manually matching up a PULSE_GEN with a PERSON. |
| 13 | `REMOVAL_DT_TM` | DATETIME |  |  | The removal date of the pulse generator |
| 14 | `SERIAL_TXT` | VARCHAR(40) |  |  | The serial number of the pulse generator |
| 15 | `SERIAL_TXT_KEY` | VARCHAR(40) |  |  | The serial number with all non-alphanumeric characters stripped out and all alphanumeric characters uppercased. |
| 16 | `TYPE_CD` | DOUBLE | NOT NULL |  | The type of pulse generator (e.g. ICD or pacemaker) |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSOC_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PULSE_GEN_PID_ID` | [PULSE_GEN_PID](PULSE_GEN_PID.md) | `PULSE_GEN_PID_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [PULSE_GEN_ASSOC_HIST](PULSE_GEN_ASSOC_HIST.md) | `PULSE_GEN_ID` |
| [PULSE_GEN_EPISODE](PULSE_GEN_EPISODE.md) | `PULSE_GEN_ID` |
| [PULSE_GEN_LEAD](PULSE_GEN_LEAD.md) | `PULSE_GEN_ID` |
| [PULSE_GEN_MEAS](PULSE_GEN_MEAS.md) | `PULSE_GEN_ID` |
| [PULSE_GEN_SESSION](PULSE_GEN_SESSION.md) | `PULSE_GEN_ID` |
| [PULSE_GEN_SET](PULSE_GEN_SET.md) | `PULSE_GEN_ID` |
| [PULSE_GEN_STAT](PULSE_GEN_STAT.md) | `PULSE_GEN_ID` |

